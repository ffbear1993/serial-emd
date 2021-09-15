%% FUNCTIONS
% Concatenation
function x = concatenate(X, d)
    [m, n] = size(X); % m: samples for each signal; n: number of signals
    a = linspace(0, 1, d + 2);
    a = a(2:d + 1)';
    b = flipud(a);
    T = flipud(X(1:d, 2:n)) .* kron(a, ones(1, n - 1)) + flipud(X(m - d + 1:m, 1:n - 1)) .* kron(b, ones(1, n - 1));
    x = [];

    for i = 1:n - 1
        x = [x; X(:, i); T(:, i)];
    end

    x = [x; X(:, n)];
end
