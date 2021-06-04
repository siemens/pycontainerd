#!/usr/bin/env python3
#
# Copyright 2019 Siemens AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
#------------
#
# watchctr -- watches containerd events in all containerd namespaces.

import grpc

from containerd.services.events.v1 import unwrap, events_pb2, events_pb2_grpc
from google.protobuf import any_pb2

import argparse

def watchctr(args):
    # Connect to containerd using the well-known containerd.sock and location.
    # Please note that this does not really connect yet, but just jots down the
    # grpc server address and the connect will only happen later when the first
    # service is to be called.
    with grpc.insecure_channel(args.containerd_address) as channel:
        print("waiting for events...")
        eventsv1 = events_pb2_grpc.EventsStub(channel)
        for ev in eventsv1.Subscribe(events_pb2.SubscribeRequest()):
            print('🖄 event type:', ev.event.type_url)
            print('⬚ namespace:', ev.namespace)
            print(unwrap(ev))

def main():
    from containerd import __api_version__
    
    parser = argparse.ArgumentParser(
        prog='watchctr',
        description='watch containerd events in all namespaces',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s ' + __api_version__,
        help='show version information and exit'
    )
    parser.add_argument(
        '--address', '-a',
        dest='containerd_address', type=str, metavar='A',
        default='unix:///run/containerd/containerd.sock',
        help='address for containerd\'s GRPC server'
    )

    args = parser.parse_args()
    watchctr(args)

if __name__ == '__main__':
    main()
