# Coursework evidence

Use these headings to organise your own results and explanations. Replace
bracketed prompts and remove unused prompts. Supplied headings are permitted
reuse; the evidence and explanation must be your own. Refer to short saved
logs rather than pasting entire CI logs.

Staff will not open your private GitHub repository. Save PR pages and CI
runs as PDFs or screenshots, with short log excerpts, in `evidence/` and
give their paths below alongside the URLs.

Complete and commit this file with your other documentation before the final
release checks. Record the final release hash, CI run and fresh-checkout outcome
in the separately submitted `SUBMISSION.txt`, outside the repository, and
submit the final CI run as a separate PDF or screenshot.

## 1. Starting point and Git review

- Starting commit: b23b85398f0930e9f573f411c6c238e67770f18e
- Reused lab files, tests and examples: calculator.py, check.sh, run.sh, README.md, REQUIREMENTS.md, test_calculator.py
- Feature branch and PR: [coursework, https://github.com/Habibkhanu/calculator/actions/runs/45630353074/job/139261538175 and saved PR file in evidence/CI-fail.png]
- Self-review: I added the division-by-zero function to test_calculator.py but had not yet written an actual test to check that it worked. I identified this during my review of the pull request. The rest of the changes looked correct.

Review outcome: I identified that a test for division by zero was still needed.


## 2. Test failure, diagnosis and fix

Plan this before fixing the chosen missing requirement or defect. An initially
missing feature is acceptable; retain the test in the final suite.

- Requirement and retained test: R2, The calculator must handle errors correctly, including division by zero.

The test checks that dividing a number by zero returns the error code DIVISION_BY_ZERO. The test is included in test_calculator.py.
- Expected result and actual failure: 
When dividing 7 by 0, the calculator should return:
("ERROR", "", "DIVISION_BY_ZERO")
The test failed because the calculator did not correctly handle division by zero.
After implementing the division-by-zero check, the same test passed.
- Before/fix commits: before(5cb60e17a0bdafdf49cb29f904d9626f691b97d0), after(1027a900207b277621d144a9bfd140452ca16b4d)
- Failing/passing local runs: ./check.sh, evidence/local-before.txt and evidence/local-after.txt
- Failing/passing CI runs:
failing url: https://github.com/Habibkhanu/calculator/actions/runs/45630353074/job/139261538175
failing hash: 5cb60e17a0bdafdf49cb29f904d9626f691b97d0
failing evidence: evidence/CI-fail.png
passing url: https://github.com/Habibkhanu/calculator/actions/runs/45717809179/job/139568281383
passing hash: 1027a900207b277621d144a9bfd140452ca16b4d
passing evidence: evidence/CI-pass.png
- CI diagnosis: The workflow was triggered by a pull request and ran on a GitHub-hosted Ubuntu runner. The division by zero job failed during the pull request step, which ran the CI pytest tests. The useful log message was: “FAILED test_calculator.py::test_divide_by_zero_returns_error - NotImplementedError: Complete process_calculation for the coursework". This showed that the division-by-zero test had failed because the calculator did not return the expected error code.
- Cause and implementation fix: The cause of the failure was that the process_calculation function had not yet been implemented and was raising a NotImplementedError. I fixed this by implementing the function to handle the four arithmetic operations, validate the input numbers and return the correct error codes. I also added a check for division by zero so that it returns DIVISION_BY_ZERO instead of causing an unhandled error. After implementing the function, I ran the tests again and they passed.

## 3. Repeatable checks and local hook

- Common check script: The check script is saved as check.sh in the main project folder. I run it locally using ./check.sh. The same script is used in GitHub Actions CI.
- Prerequisites and hook installation: 
Python 3 and pytest are required to run the tests.

I created a hooks folder and made a pre-commit file inside it. I used Nano to write the hook script, which runs ./check.sh and displays its exit code.

I then made both scripts executable and configured Git to use my hooks folder.

The commands I used were:

mkdir -p hooks
nano hooks/pre-commit
isnide the pre-commit i sued the following commands:

#!/bin/bash
./check.sh
result=$?
echo "Pre-commit exit code: $result"
exit "$result"

thenn i changed the file to make it executable:
chmod +x check.sh hooks/pre-commit
git config core.hooksPath hooks
git add hooks/pre-commit

This allows Git to run the pre-commit hook automatically before each commit. The hook file is also tracked in the repository.

- Blocked commit attempt: I made a test fail and attempted to commit. The pre-commit hook ran the tests and blocked the commit because a test failed.

Base commit hash: 684c167abef5dc652c8f59510fa46fc36b1aac42

The changes were still uncommitted after the failed attempt.

Evidence: evidence/hook-fail.txt

- Permitted commit after the fix: I fixed the failing test and attempted the commit again. All tests passed, so the hook allowed the commit.

New commit hash: b6091437d0931ebade2eeeffccda19ecae13c2a4

Evidence : evidence/hook-pass.txt

- Hook limitations and independent CI checks: The hook helps find errors before committing. However, it can be bypassed using git commit --no-verify. It also needs to be installed on each fresh checkout. GitHub Actions CI runs the same check script independently to make sure the tests are still checked even if the hook is bypassed.

## 4. Native and container batch runs

- Native normal/mixed runs: 
Native Batch Runs

I ran the batch processor from the repository root using the normal and mixed CSV files.

Normal CSV run

Command used:

python3 batch_runner.py data/normal.csv results.csv

Output:

Processed 6 records: 6 succeeded, 0 failed.

The normal CSV file processed all 6 records successfully. The output was saved in results.csv.

Mixed CSV run

Command used:

python3 batch_runner.py data/mixed.csv mixed-results.csv

Output:

Record 2: DIVISION_BY_ZERO
Record 4: UNKNOWN_OPERATION
Record 5: INVALID_NUMBER
Record 8: INVALID_NUMBER
Processed 8 records: 4 succeeded, 4 failed.

The mixed CSV file contained both valid and invalid calculations. Four records succeeded and four returned errors. The batch processor continued processing after errors, allowing later valid records to be completed.

The following evidence files were saved:

evidence/normal-run.txt
evidence/mixed-run.txt
evidence/normal-results.csv
evidence/mixed-results.csv

- Container build/run commands and image tag: [README reference or commands]
- Input/output transfer: [how files enter and leave the container]
- Mixed-run interpretation: [summary, one error and later successful records]
- Python version and Docker environment: [what you used]

## 5. Container checks in CI during development

- Checked-out source commit and CI run: [hash, URL and saved file in evidence/]
- Test gate, image build and smoke-test outcomes: [steps and results]
- Smoke fixture and expected-output check: [paths and what is asserted]
- Failure handling: [why failed tests stop the build and wrong output fails CI]

## 6. Reproduction notes

- Checkout tested during development: [commit]
- Documented setup and commands tried: [README reference]
- Outcome and any limitations: [your results]

The final fresh checkout must test the declared release commit. Record its
outcome in `SUBMISSION.txt` after the documentation is committed, CI passes
and the final commit is tagged. Do not create another commit just to insert
that commit's own hash or CI-run URL into this file.
