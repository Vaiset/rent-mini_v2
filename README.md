# RentMini v2 — Production

## Quick start on VPS
```bash
sudo apt update && sudo apt install -y git docker.io docker-compose-plugin
sudo usermod -aG docker $USER
mkdir -p /opt/rentmini && cd /opt/rentmini
git clone https://github.com/Vaiset/rent-mini_v2.git .
cp .env.example .env # fill values
docker compose up -d --build
# then issue TLS
./scripts/issue_cert.sh rentmini.org you@example.com
```

## GitHub Actions deploy
Add repo secrets: SSH_HOST, SSH_USER, SSH_KEY, PROJECT_DIR, (optional) ENV_FILE.

## API
- POST /api/auth/login-telegram?telegram_id=...&role=...
- GET /api/listings/
- POST /api/listings/?title=...&price=...&realtor_id=...
- POST /api/listings/upload (multipart file, listing_id=...)

Front: `/` and `/crm`.
