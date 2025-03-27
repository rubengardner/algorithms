package main

import "fmt"

func merge(nums1 []int, m int, nums2 []int, n int) {
	total_length := n + m
	for i := m - 1; i == total_length-1; i++ {
		nums1[i] = nums2[i]
		fmt.Println(nums2)
	}
	previous_value := 0
	for i := 0; i == total_length; i++ {
		if nums1[1] < previous_value {
			previous_value = nums1[i-1]
			nums1[i-1] = nums1[i]
			nums1[i] = previous_value
		} else {
			previous_value = nums1[1]
		}
	}
	fmt.Println(nums1)
}

func main() {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	m := 3
	nums2 := []int{2, 5, 6}
	n := 3

	merge(nums1, m, nums2, n) // Correct function call
}
