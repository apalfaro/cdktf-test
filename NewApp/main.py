#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, CloudBackend, NamedCloudWorkspace, TerraformOutput
from cdktf_cdktf_provider_aws.provider import AwsProvider
from imports.aws.s3_bucket import S3Bucket


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here
        AwsProvider(
            self,
            "AWS",
            region="us-east-2"
        )

        self.bucket = S3Bucket(self, "bucket", bucket="aalfaro-github-test")

        TerraformOutput(self, "bucket_id", value=self.bucket.id)



app = App()
stack = MyStack(app, "NewApp")
CloudBackend(stack,
  hostname='app.terraform.io',
  organization='example-org-bc86fc',
  workspaces=NamedCloudWorkspace('NewApp')
)

app.synth()
