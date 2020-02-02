#!/usr/bin/python
from lru_cache.src.distributed_cache import DistributedCache

kafka = DistributedCache.new_client()

def main():
    kafka.serve()
    print('consumendo en back')


if __name__ == '__main__':
    main()
