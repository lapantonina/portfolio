#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-

class disableCSRF:
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        return None