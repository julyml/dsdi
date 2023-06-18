/*
 *
 * Copyright 2021 gRPC authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

#import <XCTest/XCTest.h>

#import "test/runner.h"
#import "test/task.h"

// Tests in:
// libuv/test/test-getsockname.c

TEST_DECLARE(getsockname_tcp)
TEST_DECLARE(getsockname_udp)

#define TASK_LIST_START_LOCAL static task_entry_t TEST_TASKS[] = {
TASK_LIST_START_LOCAL
TEST_ENTRY(getsockname_tcp)
// TEST_ENTRY(getsockname_udp)
TASK_LIST_END

@interface LibuvGetSockNameTests : XCTestCase

@end

@implementation LibuvGetSockNameTests

- (void)testGetSockNameAll {
  for (task_entry_t* task = TEST_TASKS; task->main; task++) {
    task->main();
  }
}

@end
