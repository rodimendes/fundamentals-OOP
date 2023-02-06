docker build -t simple-electrical-circuit .

# Linha que fecha o container durante testes. Pode ser eliminada após a conclusão dos testes.
docker stop electrical_system

docker run --rm -it -d --name electrical_system simple-electrical-circuit

echo "We are inside the container electrical_system"

docker exec -it electrical_system /bin/bash
