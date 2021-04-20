#!/usr/bin/env bash

echo "::set-output name=matrix::{\"IMPL\":[\"IMPL=foo\", \"IMPL=bar basic_MODE=cbm NO_SELF_HOST=1\", \"IMPL=bar basic_MODE=qbasic NO_SELF_HOST=1\"]}"
