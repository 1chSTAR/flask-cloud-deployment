import boto3
import os
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Get details from environment variables
    cluster_name = os.environ.get('ECS_CLUSTER_NAME')
    service_name = os.environ.get('ECS_SERVICE_NAME')

    # Log the received event
    logger.info(f"Received event: {event}")

    # Create a client for the ECS API
    client = boto3.client('ecs')

    try:
        # Force a new deployment to pull the latest Docker image
        response = client.update_service(
            cluster=cluster_name,
            service=service_name,
            forceNewDeployment=True
        )
        # Log the response
        logger.info(f"Update service response: {response}")
        return {
            'statusCode': 200,
            'body': 'Service updated successfully, pulling and deploying the latest Docker image'
        }
    except Exception as e:
        # Log the exception
        logger.error(f"Error updating the service: {e}")
        return {
            'statusCode': 500,
            'body': f"Error updating the service: {str(e)}"
        }
