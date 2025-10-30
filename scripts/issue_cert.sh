#!/usr/bin/env bash
set -euo pipefail
DOMAIN="${1:-}"
EMAIL="${2:-admin@${DOMAIN}}"
if [ -z "$DOMAIN" ]; then echo 'Usage: ./scripts/issue_cert.sh domain [email]'; exit 1; fi

# ensure services up (nginx must serve /.well-known/)
docker compose up -d nginx

# obtain certificate via webroot
docker compose run --rm certbot certonly --webroot -w /var/www/certbot -d $DOMAIN -d www.$DOMAIN --email $EMAIL --agree-tos --no-eff-email

# reload nginx
docker compose exec -T nginx nginx -s reload || true
