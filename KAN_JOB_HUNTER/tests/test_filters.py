import unittest

from kan_job_hunter.filters import analyze_text, current_city


class FilterTests(unittest.TestCase):
    def test_madrid_russian_editor_with_payment(self):
        row = analyze_text("Ищем видеомонтажёра в Мадриде. Оплата 800 €. Работа на русском.")
        self.assertTrue(row["relevant"])
        self.assertEqual(row["city"], "Мадрид")
        self.assertEqual(row["language"], "русский")
        self.assertEqual(row["payment"], "800 €")

    def test_ai_and_motion_are_excluded(self):
        row = analyze_text("Ищем AI-креатора и motion designer для рекламы")
        self.assertFalse(row["relevant"])

    def test_unknown_data_is_not_invented(self):
        row = analyze_text("Нужен оператор для проекта")
        self.assertEqual(row["payment"], None)
        self.assertEqual(row["contact"], None)


if __name__ == "__main__":
    unittest.main()
