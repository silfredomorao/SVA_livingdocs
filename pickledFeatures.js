jsonPWrapper ({
  "Features": [
    {
      "RelativeFolder": "features\\Create_Segment.feature",
      "Feature": {
        "Name": "Create a New Segment",
        "Description": "All the steps involving segments creation, with scenarios of happy and sad paths",
        "FeatureElements": [
          {
            "Name": "Happy path creating a new filters",
            "Slug": "happy-path-creating-a-new-filters",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I try to create a new segment with name: \"Segment Automation\"",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I create a new Opportunity filter setup according this table",
                "TableArgument": {
                  "HeaderRow": [
                    "Amount",
                    "Field",
                    "Operator",
                    "Value",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "Annual Revenue",
                      "Type",
                      "contains",
                      "New Business",
                      "yes"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I create a new Sales filter setup according this table",
                "TableArgument": {
                  "HeaderRow": [
                    "Field",
                    "Operator",
                    "Value",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "Country",
                      "contains",
                      "US",
                      "yes"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I select the peer group filter \"Banking\"",
                "StepComments": [],
                "AfterLastStepComments": [
                  {
                    "Text": "# Sad Paths"
                  }
                ]
              }
            ],
            "Tags": [
              "@ui"
            ],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          },
          {
            "Name": "Sad path segment with no name",
            "Slug": "sad-path-segment-with-no-name",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I try to create a new segment with name: \" \"",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "the warning that \"segment name\" field is required is shown preventing continuing",
                "StepComments": [],
                "AfterLastStepComments": []
              }
            ],
            "Tags": [
              "@ui"
            ],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          },
          {
            "Name": "Sad path no peer industry selected",
            "Slug": "sad-path-no-peer-industry-selected",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I try to create a new segment with name: \"Segment Automation\"",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I create a new Opportunity filter setup according this table",
                "TableArgument": {
                  "HeaderRow": [
                    "Amount",
                    "Field",
                    "Operator",
                    "Value",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "Annual Revenue",
                      "Type",
                      "contains",
                      "New Business",
                      "yes"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I create a new Sales filter setup according this table",
                "TableArgument": {
                  "HeaderRow": [
                    "Field",
                    "Operator",
                    "Value",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "Country",
                      "contains",
                      "US",
                      "yes"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I select the peer group filter \" \"",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "the warning that \"peer name\" field is required is shown preventing continuing",
                "StepComments": [],
                "AfterLastStepComments": []
              }
            ],
            "Tags": [
              "@ui"
            ],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          },
          {
            "Name": "New segment link, actually, this is not a sad path scenario to test New segment example link",
            "Slug": "new-segment-link-actually-this-is-not-a-sad-path-scenario-to-test-new-segment-example-link",
            "Description": "without adding time to all others scenario that use segment creation",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I try to create a new segment with name: \" \"",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "the verify the new segments example link",
                "StepComments": [],
                "AfterLastStepComments": []
              }
            ],
            "Tags": [
              "@ui"
            ],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          },
          {
            "Name": "Sad path invalid opportunity filter",
            "Slug": "sad-path-invalid-opportunity-filter",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I try to create a new segment with name: \"Segment Automation\"",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I create a new Opportunity filter setup according this table",
                "TableArgument": {
                  "HeaderRow": [
                    "Amount",
                    "Field",
                    "Operator",
                    "Value",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "Annual Revenue",
                      "Type",
                      "contains",
                      "test",
                      "yes"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I cant advance and \"Opportunity warning\" msg is present",
                "StepComments": [],
                "AfterLastStepComments": []
              }
            ],
            "Tags": [
              "@ui"
            ],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          },
          {
            "Name": "Sad path invalid sales user filter",
            "Slug": "sad-path-invalid-sales-user-filter",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I try to create a new segment with name: \"Segment Automation\"",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I create a new Opportunity filter setup according this table",
                "TableArgument": {
                  "HeaderRow": [
                    "Amount",
                    "Field",
                    "Operator",
                    "Value",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "Annual Revenue",
                      "Type",
                      "contains",
                      "New Business",
                      "yes"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I create a new Sales filter setup according this table",
                "TableArgument": {
                  "HeaderRow": [
                    "Field",
                    "Operator",
                    "Value",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "Profile",
                      "contains",
                      "test",
                      "yes"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I cant advance and \"Sales warning\" msg is present",
                "StepComments": [],
                "AfterLastStepComments": [
                  {
                    "Text": "###############################"
                  }
                ]
              }
            ],
            "Tags": [
              "@ui"
            ],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          },
          {
            "Name": "To be defined deleting filters",
            "Slug": "to-be-defined-deleting-filters",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I try to create a new segment with name: \"Segment Automation\"",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I create a new Opportunity filter setup according this table",
                "TableArgument": {
                  "HeaderRow": [
                    "Amount",
                    "Field",
                    "Operator",
                    "Value",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "Annual Revenue",
                      "Type",
                      "contains",
                      "New Business",
                      "no"
                    ],
                    [
                      "Annual Revenue",
                      "Won",
                      "equals",
                      "True",
                      "no"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I delete the filter number",
                "TableArgument": {
                  "HeaderRow": [
                    "Number",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "2",
                      "yes"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "bla bla",
                "StepComments": [],
                "AfterLastStepComments": []
              }
            ],
            "Tags": [],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          },
          {
            "Name": "To be defined editing filters",
            "Slug": "to-be-defined-editing-filters",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I try to create a new segment with name: \"Segment Automation\"",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I create a new Opportunity filter setup according this table",
                "TableArgument": {
                  "HeaderRow": [
                    "Amount",
                    "Field",
                    "Operator",
                    "Value",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "Annual Revenue",
                      "Type",
                      "contains",
                      "New Business",
                      "no"
                    ],
                    [
                      "Annual Revenue",
                      "Won",
                      "equals",
                      "True",
                      "no"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I Edit the filter number:",
                "TableArgument": {
                  "HeaderRow": [
                    "Number",
                    "Field",
                    "Operator",
                    "Value",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "2",
                      "Type",
                      "contains",
                      "New Business",
                      "no"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "bla bla",
                "StepComments": [],
                "AfterLastStepComments": []
              }
            ],
            "Tags": [],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          },
          {
            "Name": "To be defined editing or deleting filter sales users",
            "Slug": "to-be-defined-editing-or-deleting-filter-sales-users",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I try to create a new segment with name: \"Segment Automation\"",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I create a new Opportunity filter setup according this table",
                "TableArgument": {
                  "HeaderRow": [
                    "Amount",
                    "Field",
                    "Operator",
                    "Value",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "Annual Revenue",
                      "Type",
                      "contains",
                      "New Business",
                      "yes"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I create a new Sales filter setup according this table",
                "TableArgument": {
                  "HeaderRow": [
                    "Field",
                    "Operator",
                    "Value",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "Country",
                      "contains",
                      "US",
                      "no"
                    ],
                    [
                      "Language",
                      "contains",
                      "English",
                      "no"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I delete the filter number",
                "TableArgument": {
                  "HeaderRow": [
                    "Number",
                    "Continue"
                  ],
                  "DataRows": [
                    [
                      "1",
                      "yes"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "bla bla",
                "StepComments": [],
                "AfterLastStepComments": []
              }
            ],
            "Tags": [],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          }
        ],
        "Result": {
          "WasExecuted": false,
          "WasSuccessful": false,
          "WasProvided": false
        },
        "Tags": []
      },
      "Result": {
        "WasExecuted": false,
        "WasSuccessful": false,
        "WasProvided": false
      }
    },
    {
      "RelativeFolder": "features\\Settings.feature",
      "Feature": {
        "Name": "Custom settings",
        "Description": "All the custom settings test scenarios",
        "FeatureElements": [
          {
            "Name": "Happy path, checking the custom settings",
            "Slug": "happy-path-checking-the-custom-settings",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "navigate into Custom Settings",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I validate verify the app configuration is according to this table",
                "TableArgument": {
                  "HeaderRow": [
                    "Name",
                    "Allow Benchmarking",
                    "Async Reports",
                    "Cron Benchmark",
                    "Cron Send Snapshot",
                    "Cron Snapshot Job",
                    "Opt In",
                    "Regression Formula"
                  ],
                  "DataRows": [
                    [
                      "AppSettings",
                      "yes",
                      "yes",
                      "0 0 0 5 * ?",
                      "0 0 0 * * ?",
                      "0 0 0 1 * ?",
                      "yes",
                      "yes"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              }
            ],
            "Tags": [
              "@smoke",
              "@ui"
            ],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          }
        ],
        "Result": {
          "WasExecuted": false,
          "WasSuccessful": false,
          "WasProvided": false
        },
        "Tags": []
      },
      "Result": {
        "WasExecuted": false,
        "WasSuccessful": false,
        "WasProvided": false
      }
    },
    {
      "RelativeFolder": "features\\Initial_Flow.feature",
      "Feature": {
        "Name": "Setup Wizard",
        "Description": "\"\"\"\r\nWith a system admin user, go into the Sales tab of the Sales Value app,\r\nthe setup flow should be displayed on the screen, click next, opt in to the terms and conditions and click next,\r\n opt into benchmarking and click next, click Let's Go\r\n\"\"\"",
        "FeatureElements": [
          {
            "Name": "Fresh Start Initial setup wizard, sad path no reading legal agreements",
            "Slug": "fresh-start-initial-setup-wizard-sad-path-no-reading-legal-agreements",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I start the setup of the assistant to add Sales Value app",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "in the legal step I try to advance and verify the condition according of readying links",
                "TableArgument": {
                  "HeaderRow": [
                    "link",
                    "expected behavior"
                  ],
                  "DataRows": [
                    [
                      "none",
                      "you must read and agree the conditions validation"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              }
            ],
            "Tags": [
              "@setup_wizard"
            ],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          },
          {
            "Name": "Fresh Start Initial setup wizard, sad path only reading research agreements",
            "Slug": "fresh-start-initial-setup-wizard-sad-path-only-reading-research-agreements",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I start the setup of the assistant to add Sales Value app",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "in the legal step I try to advance and verify the condition according of readying links",
                "TableArgument": {
                  "HeaderRow": [
                    "link",
                    "expected behavior"
                  ],
                  "DataRows": [
                    [
                      "Unified Pilot Research Agreement",
                      "Open and read both agreements."
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              }
            ],
            "Tags": [
              "@setup_wizard"
            ],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          },
          {
            "Name": "Fresh Start Initial setup wizard, sad path only reading sales exhibits",
            "Slug": "fresh-start-initial-setup-wizard-sad-path-only-reading-sales-exhibits",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I start the setup of the assistant to add Sales Value app",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "in the legal step I try to advance and verify the condition according of readying links",
                "TableArgument": {
                  "HeaderRow": [
                    "link",
                    "expected behavior"
                  ],
                  "DataRows": [
                    [
                      "Sales Value App Exhibits",
                      "Open and read both agreements."
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              }
            ],
            "Tags": [
              "@setup_wizard"
            ],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          },
          {
            "Name": "Fresh Start Initial setup wizard, happy path reading both agreements and not benchmark agreement",
            "Slug": "fresh-start-initial-setup-wizard-happy-path-reading-both-agreements-and-not-benchmark-agreement",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I start the setup of the assistant to add Sales Value app",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "in the legal step I try to advance and verify the condition according of readying links",
                "TableArgument": {
                  "HeaderRow": [
                    "link",
                    "expected behavior"
                  ],
                  "DataRows": [
                    [
                      "both",
                      "No validation is present and you can continue"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "in the benchmark step I just press next, \"without\" checking and reading the agreement",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I finish the last step of the setup wizard",
                "StepComments": [],
                "AfterLastStepComments": []
              }
            ],
            "Tags": [
              "@smoke",
              "@setup_wizard"
            ],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          },
          {
            "Name": "Fresh Start Initial setup wizard, happy path reading both agreements and benchmark agreement",
            "Slug": "fresh-start-initial-setup-wizard-happy-path-reading-both-agreements-and-benchmark-agreement",
            "Description": "",
            "Steps": [
              {
                "Keyword": "Given",
                "NativeKeyword": "Given ",
                "Name": "I successfully login in Salesforce using \"Admin\" credentials",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "I start the setup of the assistant to add Sales Value app",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "in the legal step I try to advance and verify the condition according of readying links",
                "TableArgument": {
                  "HeaderRow": [
                    "link",
                    "expected behavior"
                  ],
                  "DataRows": [
                    [
                      "both",
                      "No validation is present and you can continue"
                    ]
                  ]
                },
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "And",
                "NativeKeyword": "And ",
                "Name": "in the benchmark step I just press next, \"with\" checking and reading the agreement",
                "StepComments": [],
                "AfterLastStepComments": []
              },
              {
                "Keyword": "Then",
                "NativeKeyword": "Then ",
                "Name": "I finish the last step of the setup wizard",
                "StepComments": [],
                "AfterLastStepComments": []
              }
            ],
            "Tags": [
              "@smoke",
              "@setup_wizard"
            ],
            "Result": {
              "WasExecuted": false,
              "WasSuccessful": false,
              "WasProvided": false
            }
          }
        ],
        "Result": {
          "WasExecuted": false,
          "WasSuccessful": false,
          "WasProvided": false
        },
        "Tags": []
      },
      "Result": {
        "WasExecuted": false,
        "WasSuccessful": false,
        "WasProvided": false
      }
    }
  ],
  "Summary": {
    "Tags": [
      {
        "Tag": "@ui",
        "Total": 7,
        "Passing": 0,
        "Failing": 0,
        "Inconclusive": 7
      },
      {
        "Tag": "@smoke",
        "Total": 3,
        "Passing": 0,
        "Failing": 0,
        "Inconclusive": 3
      },
      {
        "Tag": "@setup_wizard",
        "Total": 5,
        "Passing": 0,
        "Failing": 0,
        "Inconclusive": 5
      }
    ],
    "Folders": [
      {
        "Folder": "features",
        "Total": 15,
        "Passing": 0,
        "Failing": 0,
        "Inconclusive": 15
      }
    ],
    "NotTestedFolders": [
      {
        "Folder": "features",
        "Total": 0,
        "Passing": 0,
        "Failing": 0,
        "Inconclusive": 0
      }
    ],
    "Scenarios": {
      "Total": 15,
      "Passing": 0,
      "Failing": 0,
      "Inconclusive": 15
    },
    "Features": {
      "Total": 3,
      "Passing": 0,
      "Failing": 0,
      "Inconclusive": 3
    }
  },
  "Configuration": {
    "SutName": "Sales Value App",
    "SutVersion": "1",
    "GeneratedOn": "25 junio 2020 15:38:42"
  }
});