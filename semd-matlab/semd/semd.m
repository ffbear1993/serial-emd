% Concatenated EMD

clear;
close all;

%% Here have our signals, the ones we want to decompose with EMD simultaneously
% each column is a signal, time-points are in the rows.

% some parameters...
L = 500; % length of each column (signal) that we want to decompose
u = rand(15, 1);
o1 = ones(1, L);

% Toy signals, to verify the function. Each column is a singal.
X = kron(u, o1)'; % we use kron to generate signals from u and o1, of length L
[m, n] = size(X); % m: samples for each signal (equal to L); n: number of signals
%% Our proposal (new algorithm)
% parameter of our algorithm
d = 50; % the only parameter needed. Amount of samples that we will use between each column of our signals (columns of X)
% as the transition between signals.
tic;
% Concatenating columns of X to a single column and "d" samples of transition
% between each signal
x = concatenate(X, d); % x is the vector containing all the columns plus the transitions
% figure
% plot(x) % Control plot
% title('Concatenated signals')

% EMD decomposition of x
% here we have to add the EMD decomposition
% then, each IMF will need to be desconcatenated...
[xEMD, resx] = emd(x);
all_xEMD = [xEMD, resx]; % we have to consider also the residue

% Des-concatenating of the decomposition of x
for t = 1:size(all_xEMD, 2)
    Xd(:, :, t) = deconcatenate(all_xEMD(:, t), m, n, d); % each signal is in a column, each tube is a IMF
end

X_hat = sum(Xd, 3);
tarda = toc;
disp(['Needed time: ' num2str(tarda) ' s'])

%% if we use EMD, then the sum of all IMFs of one signal has to be equal to the signal
% we expect to have a very smnall value, < e-10
sum(sum(X_hat - X))
