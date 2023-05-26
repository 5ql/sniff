function riemann_sum()
    println("Enter the function to integrate, lower and upper limits of integration, and number of subintervals (e.g., x^2, 0, 1, 100):")
    input = readline()
    f_input, a_input, b_input, n_input = split(input, ',')

    f = parse(Symbol, f_input)
    f(x) = eval(f)
    a = parse(Float64, a_input)
    b = parse(Float64, b_input)
    n = parse(Int, n_input)

    dx = (b - a) / n
    sum = 0.0
    x = a
    for i in 1:n
        sum += f(x) * dx
        x += dx
    end

    println("The Riemann sum approximation is: ", sum)
end

riemann_sum()
