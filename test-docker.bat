@echo off
echo 🐳 Testing Yegna Farms Docker Build
echo ==================================

REM Check if Docker is installed
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not installed or not in PATH
    echo Please install Docker Desktop from https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

echo ✅ Docker is available

REM Build the image
echo 🔨 Building Docker image...
docker build -t yegna-farms-test .

if %errorlevel% neq 0 (
    echo ❌ Docker build failed
    pause
    exit /b 1
)

echo ✅ Docker image built successfully

REM Run the container
echo 🚀 Starting container...
docker run -d -p 8000:8000 ^
    -e DEBUG=True ^
    -e SECRET_KEY=test-secret-key ^
    -e DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1] ^
    --name yegna-farms-test ^
    yegna-farms-test

if %errorlevel% neq 0 (
    echo ❌ Failed to start container
    pause
    exit /b 1
)

echo ✅ Container started successfully
echo 🌐 Website should be available at: http://localhost:8000
echo 👤 Admin panel: http://localhost:8000/admin (admin/admin123)

REM Wait a moment for the container to fully start
echo ⏳ Waiting for container to initialize...
timeout /t 10 /nobreak >nul

echo.
echo 📋 Useful commands:
echo   View logs: docker logs yegna-farms-test
echo   Stop container: docker stop yegna-farms-test
echo   Remove container: docker rm yegna-farms-test
echo   Remove image: docker rmi yegna-farms-test
echo.
echo 🎉 Docker test complete! Check http://localhost:8000
pause
