# cook your dish here
res = []

def solve(r, c, maze):
    if r < len(maze) and c < len(maze[0]):
        
        if maze[r][c] == 'q':
            print("sdddddddddddddd")
            print(r, c)
            return True
        elif maze[r][c] == 0:
            return False
        elif maze[r][c] == 1:
            solve(r, c+1, maze)
            solve(r+1, c, maze)
            solve(r+1, c+1, maze)

            
    return 

if __name__== '__main__':
    maze = [ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [0, 1, 0, 0], 
             [1, 1, 1, 'q']] 
    solve(0, 0, maze)
    # res.reverse()
    print(res)
    

