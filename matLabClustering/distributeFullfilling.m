function T = distributeFullfilling(D, numOfThread, threadCount, str)

n = size(D, 1);

c = ceil(n*(n-1) / ( 2* (threadCount) )) ;

positionCounter = 0;
isFoundElementPosition = false;
iPosition = 0;
jPosition = 0;
for i=1:n
    for j=i+1:n
        if positionCounter == (numOfThread-1) * c 
            isFoundElementPosition = true;
            iPosition = i;
            jPosition = j;
            break;
        end
        positionCounter = positionCounter + 1;
    end
    if isFoundElementPosition
        break;
    end;
end
positionCounter = 0;
i= int32(iPosition);
j = int32(jPosition);            
while positionCounter < c
      a = str{i};
      b = str{j};
      D(i,j) = strdist(a, b)/max(length(a), length(b));
      j = j + 1;
      if j > n
          i  = i + 1;
          j = i+1;
      end
      if i >= n 
          break;
      end
      positionCounter = positionCounter + 1;
      if mod(positionCounter, 500) == 0
          fprintf('number of thread = %d; positionCounter = %d \n', numOfThread, positionCounter)
      end
end
      
T = D;

end

