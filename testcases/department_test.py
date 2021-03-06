# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcases\department.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseDepartment(HttpRunner):

    config = (
        Config("department")
        .variables(
            **{
                "id": 1,
                "corpid": "ww85fc8a337d68c29f",
                "corpsecret": "-L8fjHHrSauoOuXn4ZMqXInzSmeUctZf150Dmz8Z03c",
            }
        )
        .base_url("https://qyapi.weixin.qq.com/cgi-bin/")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("get_token")
            .with_variables(**{"corpid": "$corpid", "corpsecret": "$corpsecret"})
            .get("gettoken")
            .with_params(**{"corpid": "$corpid", "corpsecret": "$corpsecret"})
            .with_headers(**{"User-Agent": "HttpRunner/${get_httprunner_version()}"})
            .extract()
            .with_jmespath("body.access_token", "access_token")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("department_list")
            .with_variables(**{"id": "$id"})
            .post("department/list")
            .with_params(**{"access_token": "$access_token", "id": "$id"})
            .with_headers(**{"User-Agent": "HttpRunner/${get_httprunner_version()}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("create_department")
            .with_variables(**{"id": 1})
            .post("department/create")
            .with_params(**{"access_token": "$access_token"})
            .with_headers(**{"User-Agent": "HttpRunner/${get_httprunner_version()}"})
            .with_json(
                {
                    "name": "广州研发中心",
                    "name_en": "RDGZ",
                    "parentid": 1,
                    "order": 29,
                    "id": 29,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("delete_department")
            .with_variables(**{"id": 29})
            .get("department/delete")
            .with_params(**{"access_token": "$access_token", "id": "$id"})
            .with_headers(**{"User-Agent": "HttpRunner/${get_httprunner_version()}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseDepartment().test_start()
