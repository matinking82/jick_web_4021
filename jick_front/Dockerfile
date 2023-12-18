# Use an official Node.js image as the base
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the project files to the container
COPY . .

# Build the project
RUN npm run build

# Expose the port that the application will run on
EXPOSE 3000

# Define the command to run the application
CMD ["npm", "run", "start"]
