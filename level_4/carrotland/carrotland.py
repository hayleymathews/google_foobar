from fractions import gcd

def answer(vertices):
    border_points =  (gcd(abs(vertices[0][0] - vertices[1][0]), abs(vertices[0][1] - vertices[1][1]))
                      + gcd(abs(vertices[1][0] - vertices[2][0]), abs(vertices[1][1] - vertices[2][1]))
                      + gcd(abs(vertices[2][0] - vertices[0][0]), abs(vertices[2][1] - vertices[0][1])))
    area = (.5 * abs((vertices[0][0] - vertices[2][0])
                     * (vertices[1][1] - vertices[0][1])
                     - (vertices[0][0] - vertices[1][0])
                     * (vertices[2][1] - vertices[0][1])))
    if area == 0 or border_points == 0:
        return 0
    interior_points = int(area - border_points/2 + 1)
    return(interior_points)
