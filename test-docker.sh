#!/bin/bash

echo "🐳 Testing Yegna Farms Docker Build"
echo "=================================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed or not in PATH"
    echo "Please install Docker Desktop from https://www.docker.com/products/docker-desktop"
    exit 1
fi

echo "✅ Docker is available"

# Build the image
echo "🔨 Building Docker image..."
docker build -t yegna-farms-test .

if [ $? -ne 0 ]; then
    echo "❌ Docker build failed"
    exit 1
fi

echo "✅ Docker image built successfully"

# Run the container
echo "🚀 Starting container..."
docker run -d -p 8000:8000 \
    -e DEBUG=True \
    -e SECRET_KEY=test-secret-key \
    -e DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1] \
    --name yegna-farms-test \
    yegna-farms-test

if [ $? -ne 0 ]; then
    echo "❌ Failed to start container"
    exit 1
fi

echo "✅ Container started successfully"
echo "🌐 Website should be available at: http://localhost:8000"
echo "👤 Admin panel: http://localhost:8000/admin (admin/admin123)"

# Wait a moment for the container to fully start
echo "⏳ Waiting for container to initialize..."
sleep 10

# Test if the website is responding
echo "🧪 Testing website response..."
if curl -f http://localhost:8000 > /dev/null 2>&1; then
    echo "✅ Website is responding!"
    echo "🎉 Docker test successful!"
else
    echo "⚠️ Website might still be starting up..."
    echo "Check manually at http://localhost:8000"
fi

echo ""
echo "📋 Useful commands:"
echo "  View logs: docker logs yegna-farms-test"
echo "  Stop container: docker stop yegna-farms-test"
echo "  Remove container: docker rm yegna-farms-test"
echo "  Remove image: docker rmi yegna-farms-test"
