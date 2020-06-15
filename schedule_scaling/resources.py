""" Overrides of Kubernetes resource classes from pykube """
import pykube

class Deployment(pykube.Deployment):
    """ Extends pykube.Deployment, overriding k8s apiVersion 'extensions/v1beta1' with 'apps/v1' """
    version = "apps/v1"
