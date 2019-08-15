start-dev:
	bash -c 'trap "" SIGINT SIGTERM ERR; docker-compose -f docker-compose-dev.yml -p aclu up'

stop-dev:
	bash -c 'trap "" SIGINT SIGTERM ERR; docker-compose -f docker-compose-dev.yml -p aclu down'

prod:
	bash -c 'trap "" SIGINT SIGTERM ERR; docker-compose -f docker-compose-dev.yml -p aclu up'

stop-prod:
	bash -c 'trap "" SIGINT SIGTERM ERR; docker-compose -f docker-compose-dev.yml -p aclu up'

create-volume:
	bash -c 'trap "" SIGINT SIGTERM ERR; docker volume create aclu-db'

delete-volume:
	bash -c 'trap "" SIGINT SIGTERM ERR; docker volume rm aclu-db'
