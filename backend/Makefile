start-dev:
	bash -c 'trap "" SIGINT SIGTERM ERR; docker-compose -f docker-compose-dev.yml -p aclu up'

stop-dev:
	bash -c 'trap "" SIGINT SIGTERM ERR; docker-compose -f docker-compose-dev.yml -p aclu down'

prod:
	bash -c 'trap "" SIGINT SIGTERM ERR; docker-compose -f docker-compose.yml -p aclu up'

stop-prod:
	bash -c 'trap "" SIGINT SIGTERM ERR; docker-compose -f docker-compose.yml -p aclu down'

