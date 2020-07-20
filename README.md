# squid-federations
⚗️  graphql gateway with federated schema flask servers and mongoengine integration


# Build Project 

    ./build.sh

# Docker Compose File

    version : "3"

    services:
        # Graphql Apollo Api Gateway
        gateway:
            build:
                context: ./api-gateway
                dockerfile: ./Dockerfile
            depends_on:
                - service1
                - service2
            restart: on-failure:50
            ports:
            - 1000:80

        # Graphql Federation Microservices
        service1:
            build:
                context: ./service1
                dockerfile: ./Dockerfile
            ports:
                - 1001:80

        service2:
            build:
                context: ./service2
                dockerfile: ./Dockerfile
            ports:
                - 1002:80

    
