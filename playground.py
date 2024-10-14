import ray

# Initialize Ray
if ray.is_initialized():
    ray.shutdown()
ray.init()

print(ray.cluster_resources())