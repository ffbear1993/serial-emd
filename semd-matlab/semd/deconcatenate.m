% Des-concatenation
function X = deconcatenate(x, m, n, d)
    % Input parameters:
    % x: concatenated signal (will need to be called for each IMF)
    % (could be vectorized and improved to be done altogether, but IMF by IMF allows us to have more control on it)
    % m: original length of the signals
    % n: number of signals concatenated
    % d: number of transition samples

    % Output parameters:
    % X: original matrix (each column is a signal)

    X = zeros(m, n);

    for i = 1:n - 1
        X(:, i) = x(1 + (i - 1) * (m + d):m + (i - 1) * (m + d));
    end

    X(:, n) = x(1 + (n - 1) * (m + d):m + (n - 1) * (m + d));
end
