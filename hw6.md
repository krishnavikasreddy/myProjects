**Hypothesis**

-   H<sub>0</sub> : &beta;<sub>1</sub> = 0
-   H<sub>a</sub> : &beta;<sub>1</sub> &ne; 0

**Parameters**

-   &alpha; = 0.01
-   n = 84 [nrow(crimes)]

**F Test**

-   For the given &alpha; and n we require that
    -   F\* &le; F(0.99:1,82) = [qf(0.99,1,82)] = 6.95442 => conclude H<sub>0</sub>
    -   F\* > F(0.99:1,82) = [qf(0.99,1,82)] = 6.95442 => conclude H<sub>a</sub>
-   From anova Table we got F = 16.834 > 6.95442 thus conclude H<sub>a</sub>

**Decision**

-   Evidence prove that we can conclude H<sub>a</sub> thus we there is a relation between crimes and Education data

-   we know that
    -   F\* = \(\frac{MSR}{MSE}\)
        -   MSR = \(\frac{SSR}{df_r}\) = \(\frac{SSR}{1}\) = b<sub>1</sub><sup>2</sup> &sum;(X<sub>i</sub> - \(\overline{X}\))<sup>2</sup>
        -   MSE = s<sup>2</sup>{b<sub>1</sub>} &sum;(X<sub>i</sub> - \(\overline{X}\))<sup>2</sup>
    -   F\* = \(\frac{b_1^2}{{s^2{b_1}}}\) = (t\*)<sup>2</sup>

-   We need to know two points t\* represents a two tailed test while as F\* is a one tailed test
    -(t\*(1-&alpha;/2:n-1))<sup>2</sup> = f\*(1-&alpha;,1,n-2)

**Hypothesis**

-   H<sub>o</sub> : &beta;<sub>1</sub> = 0
-   H<sub>a</sub> : &beta;<sub>1</sub> &ne; 0

-   Full model(we reject Null hypothesis => H<sub>a</sub> is true => &beta;<sub>1</sub> &ne; 0)
    -   CrimeRate(Y<sub>i</sub>) = &beta;<sub>0</sub> + &beta;<sub>1</sub> \* Education(X<sub>i</sub>) + &epsilon;<sub>i</sub>
-   Reduced Model (We assume that Null Hypothesis is True => &beta;<sub>1</sub> = 0)
    -   CrimeRate(Y<sub>i</sub>) = &beta;<sub>0</sub> + &epsilon;<sub>i</sub>

-   SSE(F) = &sum;&epsilon;<sub>i</sub><sup>2</sup>{F} = &sum;(Y - &beta;<sub>0</sub> - &beta;<sub>1</sub> \* X<sub>i</sub>)<sup>2</sup> = &sum;(Y - \(\hat{Y}\))<sup>2</sup> = {aModel[2,"Sum Sq"]} = 455273165

-   SSE(R) = &sum;&epsilon;<sub>i</sub><sup>2</sup>{R} = &sum;(Y<sub>i</sub>- &beta;<sub>0</sub>)<sup>2</sup> = &sum;(Y<sub>i</sub> - $\bar{Y})<sup>2</sup> = SSTO = {sum(aModel["Sum Sq"])} = 548736108

-   df<sub>F</sub> = we have two variables that determine our Y = &beta;<sub>0</sub> and &beta;<sub>1</sub> so =  n-2

-   df<sub>R</sub> = we have only one variable that affect our Y = &beta;<sub>0</sub> = n-1
