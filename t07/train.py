import torch
from torch import nn

torch.manual_seed(20260907)

X = torch.randn(1000, 2)
y = (X[:, 0] + X[:, 1] > 0).float().reshape(-1, 1)

X_train = X[:800]
y_train = y[:800]

X_test = X[800:]
y_test = y[800:]

model = nn.Linear(2, 1)

loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(500):
    logits = model(X_train)
    loss = loss_fn(logits, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f"epoch {epoch + 1}: loss = {loss.item():.6f}")

model.eval()

with torch.no_grad():
    logits = model(X_test)
    prob = torch.sigmoid(logits)
    pred = (prob >= 0.5).float()

    accuracy = (pred == y_test).float().mean()

print("final loss:", loss.item())
print("test accuracy:", accuracy.item())
print("weight:", model.weight.detach())
print("bias:", model.bias.detach())