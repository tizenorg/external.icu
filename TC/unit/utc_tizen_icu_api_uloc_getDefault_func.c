/*
 *  tizen-icu-api
 *
 * Copyright (c) 2000 - 2012 Samsung Electronics Co., Ltd. All rights reserved.
 *
 * Contact: Jayoun Lee <airjany@samsung.com>
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

#include <tet_api.h>
#include <unicode/utypes.h>
#include <unicode/uloc.h>
#include <unicode/ucal.h>
#include <unicode/udat.h>
#include <unicode/unum.h>
#include <unicode/ucnv.h>
#include <unicode/ustring.h>
#include <unistd.h>
#include<unicode/utmscale.h>

static void startup(void);
static void cleanup(void);

void (*tet_startup) (void) = startup;
void (*tet_cleanup) (void) = cleanup;

static void utc_tizen_icu_api_uloc_getDefault_func_01(void);

enum {
	POSITIVE_TC_IDX = 0x01,
	NEGATIVE_TC_IDX,
};

struct tet_testlist tet_testlist[] = {
	{utc_tizen_icu_api_uloc_getDefault_func_01, POSITIVE_TC_IDX},
	{NULL, 0}
};

static void startup(void)
{
	tet_infoline("Testing API utc_tizen_icu_api_uloc_getDefault start");
	return;
}

static void cleanup(void)
{
	tet_infoline("Testing API utc_tizen_icu_api_uloc_getDefault ends ");
	return;
}

/**
 * @brief Positive test case of utc_tizen_icu_api_uloc_getDefault()
 */
static void utc_tizen_icu_api_uloc_getDefault_func_01(void)
{
	const char *result = NULL;
	result = uloc_getDefault();

	if (NULL != result) {
		tet_infoline("utc_tizen_icu_api_uloc_getDefault test PASS!");
		tet_printf("Default locale %s\n", result);
		tet_result(TET_PASS);
	} else {
		tet_infoline("utc_tizen_icu_api_uloc_getDefault test FAIL!");
		tet_result(TET_FAIL);
	}
	return;
}
