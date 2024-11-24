# message-blaster

### 1. Setup environment
Install the dependencies with requirements.lock.
```
rye sync
```

### 2. Start docker
Build image and start docker compose service.
```
docker compose up -d -build
```

### 3. Migration on database
```
docker compose exec django-1 bash
python manage.py migrate
```

### 4. Create superuser
```
docker compose exec django-1 bash
python manage.py createsuperuser
```

### 5. Check server running successfully
http://localhost:8000