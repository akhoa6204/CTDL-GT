# def isPalindrome(s):
#     def tochars(s):
#         s=s.lower()
#         ans=''
#         for c in s:
#             if c in 'abcdefghijklmnopqrstuvwxyz':
#                 ans=ans+c
#         return ans
#     def isPal(s):
#         print('Kiem tra doi xung chuoi '+str(s))
#         if len(s) <=1: 
#             return True
#         else :
#             return s[0]==s[-1] and isPal(s[1:-1])
#             #kiểm tra kí tự đầu và cuối xem giống nhau
#             #nếu giống nhau thì đệ qui bỏ đi kí tự đầu và kí tự cuối của chuỗi hiện tại
#             #và tiếp tục kiểm tra khi chuỗi còn độ dài <=1 
#     return isPal(tochars(s))
# isPalindrome('ABCba')
# isPalindrome('abc,.,...def')
def kiemthu(s):
    def b1(s):
        s=s.lower()
        ans=''
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans+=c
        return ans
    def b2(s):
        while True : 
            if len(s)<=1:
                break
            print('kiem thu chuoi: '+str(s)) 
            if s[0]==s[-1]:
                s=s[1:-1]
                print(True)
                continue
            else : 
                print(False)
                break 
    return b2(b1(s))
kiemthu("abccba")
# b1 có 1 vòng lặp for worstcase là n
# b2 có 1 vòng lặp worstcase là n - các chữ không phải là số <=> n 
# =>  ĐỘ phức tạp : O(n)+O(n)=O(2n)==O(n)