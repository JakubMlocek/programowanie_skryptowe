import main
import unittest

class TestCourses(unittest.TestCase):
    def test_add_course(self):
        courses = {"klocki":["jakmlo","jaga","kochan"]}
        coursesfinal = {"klocki":["jakmlo","jaga","kochan"],"babiloni":[]}
        main.add_course("babiloni",courses,20)
        print(courses)
        print(coursesfinal)
        self.assertDictEqual(courses,coursesfinal)

    def test_exceed_course_limit(self):
        courses = {"klocki":["jakmlo","jaga","kochan"],"babiloni":["asd"]}
        coursesfinal = {"klocki":["jakmlo","jaga","kochan"],"babiloni":["asd"]}
        main.add_course("omgei",courses,2)
        self.assertDictEqual(courses,coursesfinal)

    def test_remove_course(self):
        coursesfinal = {"klocki":["jakmlo","jaga","kochan"]}
        courses = {"klocki":["jakmlo","jaga","kochan"],"babiloni":[]}
        main.remove_course("babiloni", courses)
        self.assertDictEqual(courses,coursesfinal)


    def test_add_pearson_to_course(self):
        courses = {"klocki":["jakmlo","jaga","kochan"],"babiloni":["domo","aug"]}
        coursesfinal = {"klocki":["jakmlo","jaga","kochan"],"babiloni":["domo","aug","ryba"]}
        main.add_pearson_to_course("ryba","babiloni",courses,20)
        self.assertDictEqual(courses,coursesfinal)

    def test_exceed_pearson_limit_in_course(self):
        courses = {"klocki":["jakmlo","jaga","kochan"],"babiloni":["domo","aug"]}
        coursesfinal = {"klocki":["jakmlo","jaga","kochan"],"babiloni":["domo","aug"]}
        main.add_pearson_to_course("ryba","klocki",courses,3)
        self.assertDictEqual(courses,coursesfinal)

    def test_remove_pearson_from_course(self):
        courses = {"klocki":["jakmlo","jaga","kochan"],"babiloni":["domo","aug","ryba"]}
        coursesfinal = {"klocki":["jakmlo","jaga","kochan"],"babiloni":["domo","aug"]}
        main.remove_pearson_from_course("ryba","babiloni",courses)
        self.assertDictEqual(courses,coursesfinal)
    
    def test_remove_pearson_that_not_exist_in_course(self):
        courses = {"klocki":["jakmlo","jaga","kochan"],"babiloni":["domo","aug","ryba"]}
        coursesfinal = {"klocki":["jakmlo","jaga","kochan"],"babiloni":["domo","aug","ryba"]}
        main.remove_pearson_from_course("ebe","babiloni",courses)
        self.assertDictEqual(courses,coursesfinal)

    def test_modify_course(self):
        courses = {"klocki":["jakmlo","jaga","kochan"],"babiloni":["domo","aug","ryba"]}
        coursesfinal = {"klocki":["jakmlo","jaga","kochan"],"kapitolni":["domo","aug","ryba"]}
        main.modify_course("babiloni","kapitolni", courses)
        self.assertDictEqual(courses,coursesfinal)



if __name__ == '__main__':
    unittest.main()
