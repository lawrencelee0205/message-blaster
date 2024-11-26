from telethon import TelegramClient
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PhoneNumberForm, VerificationCodeForm, MessageForm
import asyncio

async def async_request_phone_number(telegram_api_id, telegram_api_hash, sender_phone_number, target_phone_number, message="Hi"):
    client = TelegramClient('session_name', telegram_api_id, telegram_api_hash)
    await client.connect()
    sent_code = await client.send_code_request(sender_phone_number)
    return sent_code

def request_phone_number(request):
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            telegram_api_id, telegram_api_hash = settings.TELEGRAM_API_ID, settings.TELEGRAM_API_HASH
            sent_code = asyncio.run(async_request_phone_number(telegram_api_id, telegram_api_hash, phone_number, '+601130714856'))
            request.session['phone_number'] = phone_number
            request.session['phone_code_hash'] = sent_code.phone_code_hash
            return redirect('verify_code')
    else:
        form = PhoneNumberForm()
    
    return render(request, 'message/request_phone.html', {'form': form})

async def async_verify_code(telegram_api_id, telegram_api_hash, phone_number, code, phone_code_hash):
    client = TelegramClient('session_name', telegram_api_id, telegram_api_hash)
    await client.connect()
    await client.sign_in(phone=phone_number, code=code, phone_code_hash=phone_code_hash)

def verify_code(request):
    if request.method == 'POST':
        form = VerificationCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            phone_number = request.session.get('phone_number')
            phone_code_hash = request.session.get('phone_code_hash')
            telegram_api_id, telegram_api_hash = settings.TELEGRAM_API_ID, settings.TELEGRAM_API_HASH
            try:
                asyncio.run(async_verify_code(telegram_api_id, telegram_api_hash, phone_number, code, phone_code_hash))
                return redirect('send_message')
            except Exception as e:
                return HttpResponse(f"Failed to sign in: {e}")

    else:
        form = VerificationCodeForm()
    
    return render(request, 'message/verify_code.html', {'form': form})

async def async_send_message(telegram_api_id, telegram_api_hash, phone_number, message):
    client = TelegramClient('session_name', telegram_api_id, telegram_api_hash)
    await client.connect()
    await client.send_message("+601130714856", message)

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            phone_number = request.session.get('phone_number')
            telegram_api_id, telegram_api_hash = settings.TELEGRAM_API_ID, settings.TELEGRAM_API_HASH
            asyncio.run(async_send_message(telegram_api_id, telegram_api_hash, phone_number, message))
            return HttpResponse("Message sent successfully!")
    else:
        form = MessageForm()
    
    return render(request, 'message/send_message.html', {"form": form})