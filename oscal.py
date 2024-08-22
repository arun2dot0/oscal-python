from oscal_pydantic import complete  # Import the complete OSCAL schema
import json
import uuid
from datetime import datetime

# Load Trivy JSON results
with open('results.json', 'r') as file:
    trivy_results = json.load(file)

# Create a basic OSCAL component definition
# Adjust the structure based on the actual library
oscal_component = complete.ComponentDefinition(
    uuid=str(uuid.uuid4()),  # Generate a unique UUID
    metadata=complete.PublicationMetadata(
        title="Trivy Scan Results",
        last_modified=datetime.now().isoformat(),
        version="1.0",
        oscal_version="1.0.0",
        remarks="Generated from Trivy scan results"
    ),
    components=[
        complete.Component(
            uuid=str(uuid.uuid4()),  # Generate a unique UUID
            type="software",
            title="Container Image Vulnerabilities",
            description="Vulnerabilities found in container image",
            props=[
                complete.Property(
                    name="vulnerability",
                    value=json.dumps(trivy_results)  # Embed Trivy results as a property
                )
            ]
        )
    ]
)

# Export the OSCAL component definition to JSON
# oscal_json = oscal_component.model_dump_json(indent=2)

oscal_json = oscal_component.json()

# Save the OSCAL JSON to a file
with open('oscal_results.json', 'w') as file:
    file.write(oscal_json)

print("OSCAL report generated successfully.")