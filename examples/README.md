# Examples

The examples in this directory have to be run as root in order to be able to
successfully connect to the local `containerd` instance.

- `lsctr.py` lists all containers in all `containerd` namespaces. It's kind of
  `ctr c ls` on drugs, automatically discovering all namespaces and then listing
  containers in each one.

- `watchctr.py` waits for `containerd` events, such as creating or deleting
  containers and tasks, et cetera, and prints them to the console as they
  happen.
