import boto3, json

client = boto3.client('apigateway', region_name='us-east-1')


api_id = client.get_rest_apis()['items'][0]['id']


response = client.get_resources(restApiId=api_id)
resource_id = None
for resource in response['items']:
    if resource.get('path') == "/memberships":
        resource_id = resource['id']
        break
parent_id = resource_id

memberships = client.create_resource(
    restApiId=api_id,
    parentId=parent_id,
    pathPart='popular'
)
memberships_resource_id = memberships["id"]


product_method = client.put_method(
    restApiId=api_id,
    resourceId=memberships_resource_id,
    httpMethod='GET',
    authorizationType='NONE'
)

product_response = client.put_method_response(
    restApiId=api_id,
    resourceId=memberships_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': True,
        'method.response.header.Access-Control-Allow-Origin': True,
        'method.response.header.Access-Control-Allow-Methods': True
    },
    responseModels={
        'application/json': 'Empty'
    }
)

product_integration = client.put_integration(
    restApiId=api_id,
    resourceId=memberships_resource_id,
    httpMethod='GET',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)


product_integration_response = client.put_integration_response(
    restApiId=api_id,
    resourceId=memberships_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseTemplates={
        "application/json": json.dumps({
            "membership_item_arr": [{
                "membership_name_str": "gold",
                "membership_id_str": "m003",
                "price_in_cents_int": 5999,
                "description_str": "Acceso completo, asesorías personalizadas y sauna.",
                "special_int": 1,
                "tag_str_arr": ["popular","limitado"]
                }]
        })
    },
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        'method.response.header.Access-Control-Allow-Methods': "'GET'",
        'method.response.header.Access-Control-Allow-Origin': "'*'"
    }
)


print ("DONE")

"""
Copyright @2021 [Amazon Web Services] [AWS]
    
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
