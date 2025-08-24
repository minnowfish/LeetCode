// Maybe I will try another solution using match instead of HashMap

use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let mut i = 0;
        let mut result : i32 = 0;

        let roman_numerals = HashMap::from([
            ('I' , 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)
        ]);

        for i in 0..s.len() {
            let current = roman_numerals[&s[i]];
            if i + 1 < s.len(){
                let next = roman_numerals[&s[i + 1]];
                if current < next {
                    result -= current;
                    continue
                }
            }
            result += current;
        }
        result
    }
}
