from typing import Any
from unittest import TestCase

test_case = TestCase()


class AssertMixin:
    @staticmethod
    def assertEqual(first: Any, second: Any) -> None: 
        test_case.assertEqual(first, second)

    @staticmethod    
    def assertFalse(expr: Any) -> None: 
        test_case.assertFalse(expr)

    @staticmethod
    def assertTrue(expr: Any) -> None: 
        test_case.assertTrue(expr)

    @staticmethod
    def assertIsNone(obj: object) -> None: 
        test_case.assertIsNone(obj) 

    @staticmethod
    def assertIsNotNone(obj: object) -> None: 
        test_case.assertIsNotNone(obj)
