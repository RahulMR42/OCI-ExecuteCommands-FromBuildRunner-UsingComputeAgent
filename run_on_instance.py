# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
compute_instance_agent_client = oci.compute_instance_agent.ComputeInstanceAgentClient(
    config)


# Send the request to service, some parameters are not required, see API
# doc for more info
create_instance_agent_command_response = compute_instance_agent_client.create_instance_agent_command(
    create_instance_agent_command_details=oci.compute_instance_agent.models.CreateInstanceAgentCommandDetails(
        compartment_id="ocid1.compartment.oc1..aaaaaaaalbagydl2powatrvczfdfempy5z5j7g7kjm3gp6lkuk2odvvsrvdq",
        execution_time_out_in_seconds=854,
        target=oci.compute_instance_agent.models.InstanceAgentCommandTarget(
            instance_id="ocid1.instance.oc1.iad.anuwcljrk56z2vqcxm7yzegqb7llv773oronkaijbrrtefu7a653esoycdhq"),
        content=oci.compute_instance_agent.models.InstanceAgentCommandContent(
            source=oci.compute_instance_agent.models.InstanceAgentCommandSourceViaObjectStorageUriDetails(
                source_type="OBJECT_STORAGE_URI",
                source_uri="EXAMPLE-sourceUri-Value"),
            output=oci.compute_instance_agent.models.InstanceAgentCommandOutputViaObjectStorageTupleDetails(
                output_type="OBJECT_STORAGE_TUPLE",
                bucket_name="EXAMPLE-bucketName-Value",
                namespace_name="EXAMPLE-namespaceName-Value",
                object_name="EXAMPLE-objectName-Value")),
        display_name="EXAMPLE-displayName-Value"),
    opc_request_id="YFMGGBX3FUKQBU7O3WKU<unique_ID>",
    opc_retry_token="EXAMPLE-opcRetryToken-Value")

# Get the data from response
print(create_instance_agent_command_response.data)