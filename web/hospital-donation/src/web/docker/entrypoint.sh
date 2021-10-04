#!/usr/bin/env sh
echo "Run apps"
pm2 start ${MAIN_APP} -i ${NUM_WORKER}

echo "Run NGINX in foreground"
nginx -g 'daemon off;'