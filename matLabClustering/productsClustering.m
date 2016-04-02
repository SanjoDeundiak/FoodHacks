% please change the name of the file
fl = fopen('test.txt','r');


items = textscan(fl, '%s', 'Delimiter', '\n');
str = unique(items{1,1});
numOfEl = numel(str);

fclose(fl); %close file.

%# create and fill upper half only of distance matrix
%oldD = zeros(numOfEl,numOfEl);
D = zeros(numOfEl,numOfEl);
newD = zeros(numOfEl,numOfEl);

threadCount = int16(2); 
parpool(threadCount);
parfor i = 1:threadCount
    D = D + distributeFullfilling(newD, i, threadCount, str);
end
delete(gcp);
D = D + D';

% for i=1:numOfEl
%     for j=i+1:numOfEl
%         a = str{i};
%         b = str{j};
%         oldD(i,j) = strdist(a, b)/max(length(a), length(b));
%     end
% end
% D = D + D';       %'# symmetric distance matrix
% oldD = oldD + oldD';      
%# linkage expects the output format to match that of pdist,
%# so we convert D to a row vector (lower/upper part of matrix)
D = squareform(D, 'tovector');
% oldD = squareform(oldD, 'tovector');

% [deviation, indDev] = max(abs(D - oldD));

Z = linkage(D, 'ward');

% here 0.5 is a threshold for the cutting clustered tree acoording to the
% height
clusteredTree = cluster(Z, 'Cutoff', 0.3*max(Z(:,3)));
% figure;
% plot(Z(:,3));
% figure;
% plot(diff(Z(:,3)));
%numOfClusters = max(clusteredTree); 
%figure;
%[H,T] = dendrogram(Z, 'colorthreshold', 'default') ;
stringAndCluster = cell(numOfEl, 2);
stringAndCluster(:,1) =  str;
stringAndCluster(:, 2) = num2cell(clusteredTree);

fid=fopen('productsClasters.csv','wt');
[rows,cols]=size(stringAndCluster);

for i=1:rows
      fprintf(fid,'%s,',stringAndCluster{i,1:end-1});
      fprintf(fid,'%d\n',stringAndCluster{i,end});
end

fclose(fid);