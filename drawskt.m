%USAGE: drawskt(1,3,1,4,1,2) --- show actions 1,2,3 performed by subjects 1,2,3,4 with instances 1 and 2.
function drawskt(skeleton)

skeleton = permute(skeleton, [1 3 2]);

X=skeleton(:,:,1);
Z=skeleton(:,:,2);
Y=skeleton(:,:,3);

J = [ 1 2 3 3 5 6 7 3  9 10 11  1  1 13 14 15 17 18 19 13;
      2 3 4 5 6 7 8 9 10 11 12 13 17 14 15 16 18 19 20 17];
figure(1);
for s=1:size(X,2)
    S=[X(:,s) Y(:,s) Z(:,s)];
  
    xlim = [0 800];
    ylim = [0 800];
    zlim = [0 800];
    set(gca, 'xlim', xlim, ...
             'ylim', ylim, ...
             'zlim', zlim);

    h=plot3(S(:,1),S(:,2),S(:,3),'r.');
    %rotate(h,[0 45], -180);
    set(gca,'DataAspectRatio',[1 1 1]);
    %axis([-1 1 3 4 -1 1]);
    %axis([-1 1 -1 1 -1 1]);
    
    for j=1:20
        c1=J(1,j);
        c2=J(2,j);
        line([S(c1,1) S(c2,1)], [S(c1,2) S(c2,2)], [S(c1,3) S(c2,3)]);
         if j == 20
             line([S(c1,1) S(c2,1)], [S(c1,2) S(c2,2)], [S(c1,3) S(c2,3)],'color','r');
         end
    end
    pause(1/20)
end