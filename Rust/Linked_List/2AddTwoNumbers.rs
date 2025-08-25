// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode::new(0));
        let mut tail = &mut dummy;
        let mut l1 = l1;
        let mut l2 = l2;
        let mut carry : i32 = 0;

        while l1.is_some() || l2.is_some() || carry > 0{
            let mut digit1 : i32 = 0;
            let mut digit2 : i32 = 0;
            let mut sum : i32;
            if let Some(node1) = l1 {
                digit1 = node1.val;
                l1 = node1.next
            }

            if let Some(node2) = l2 {
                digit2 = node2.val;
                l2 = node2.next
            }

            
            sum = digit1 + digit2 + carry;
            let mut new_digit = sum % 10;
            tail.as_mut().next = Some(Box::new(ListNode::new(new_digit)));
            tail = tail.as_mut().next.as_mut().unwrap();

            carry = sum / 10;
        }

        dummy.next
    }
}
