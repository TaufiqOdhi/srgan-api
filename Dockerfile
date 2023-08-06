FROM srgan-api:req

WORKDIR /app

COPY . .

# Expose the port that Uvicorn will be listened on
EXPOSE 8000

# Run the Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]