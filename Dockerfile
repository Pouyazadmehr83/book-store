# Pull base image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/requirements.txt

# Install dependencies with custom mirror
RUN pip install --no-cache-dir -i https://mirror-pypi.runflare.com/simple -r requirements.txt

# Copy project (تغییر: کل پروژه در /code کپی می‌شود)
COPY . /code/