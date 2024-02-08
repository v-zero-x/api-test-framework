# Troublshooting Tips

## 1. Accessing the API Container

First, ensure your API container is running. If you're unsure of the container's name or ID, you can list all running containers:

```bash
docker ps
```

Look for the container running your Flask application. You'll use its name or ID in the next steps.

## 2. Executing Commands Inside the API Container

To interact with your Flask application inside its Docker container, use `docker exec` to run commands inside the container. Here's how to open a shell:

```bash
docker exec -it <container_name_or_id> /bin/sh
```

Replace `<container_name_or_id>` with the actual name or ID of your running API container.

## 3. Testing API Endpoints with `curl`

Once inside the container, you can use `curl` to make requests to your Flask application. Since you're inside the container, you'll target the application using `localhost` and the port it's running on (assuming it's `5000` based on your Docker setup).

### Installing `curl` Temporarily

If your Docker container is based on a Debian/Ubuntu image, you can install `curl` using `apt`. If it's based on Alpine, you can use `apk`. Note that changes made in this way will be lost when the container is stopped unless you commit the changes to a new image. However, for temporary testing purposes, this is often sufficient.

For a Debian/Ubuntu-based container:

```bash
apt-get update && apt-get install -y curl
```

### Get All Items

```bash
curl http://localhost:5000/items
```

### Create an Item

```bash
curl -X POST http://localhost:5000/items -H "Content-Type: application/json" -d '{"name": "New Item"}'
```

### Update an Item

First, ensure you have an item with the ID you intend to update. If you're using `1`, replace `<id>` with `1`:

```bash
curl -X PUT http://localhost:5000/items/<id> -H "Content-Type: application/json" -d '{"name": "Updated Item Name"}'
```

### Delete an Item

Similarly, ensure the item exists before attempting to delete:

```bash
curl -X DELETE http://localhost:5000/items/<id>
```

## Notes

- **API vs. Tester Container**: These commands are meant to be run in the **API container**, not the tester container, because you're directly interacting with the Flask application.
- **Adjusting Port Numbers**: If your Flask application inside Docker listens on a different port, adjust the `curl` commands accordingly.
- **Shell Availability**: The command to access the shell (`/bin/sh`) assumes a Unix-like shell is available in your container. If your Docker image is based on a minimal or non-standard base image, you might need to adjust this command.

