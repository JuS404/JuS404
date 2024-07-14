local UIS = game:GetService("UserInputService")
local RunService = game:GetService("RunService")
local player = game.Players.LocalPlayer

-- Create GUI
local ScreenGui = Instance.new("ScreenGui", player:WaitForChild("PlayerGui"))
local Frame = Instance.new("Frame", ScreenGui)
Frame.Size = UDim2.new(0, 220, 0, 200)
Frame.Position = UDim2.new(0, 50, 0, 50)
Frame.BackgroundColor3 = Color3.fromRGB(50, 50, 50)
Frame.Active = true
Frame.Draggable = true

local ToggleButton = Instance.new("TextButton", Frame)
ToggleButton.Size = UDim2.new(0, 180, 0, 40)
ToggleButton.Position = UDim2.new(0, 20, 0, 10)
ToggleButton.Text = "Toggle FOV"
ToggleButton.BackgroundColor3 = Color3.fromRGB(100, 100, 100)
ToggleButton.TextColor3 = Color3.fromRGB(255, 255, 255)

local FovColorPicker = Instance.new("TextBox", Frame)
FovColorPicker.Size = UDim2.new(0, 180, 0, 40)
FovColorPicker.Position = UDim2.new(0, 20, 0, 60)
FovColorPicker.PlaceholderText = "FOV Color (R,G,B)"
FovColorPicker.BackgroundColor3 = Color3.fromRGB(100, 100, 100)
FovColorPicker.TextColor3 = Color3.fromRGB(255, 255, 255)

local SizeSlider = Instance.new("TextBox", Frame)
SizeSlider.Size = UDim2.new(0, 180, 0, 40)
SizeSlider.Position = UDim2.new(0, 20, 0, 110)
SizeSlider.PlaceholderText = "FOV Size (Radius)"
SizeSlider.BackgroundColor3 = Color3.fromRGB(100, 100, 100)
SizeSlider.TextColor3 = Color3.fromRGB(255, 255, 255)

-- Create FOV Circle
local FovCircle = Drawing.new("Circle")
FovCircle.Radius = 30
FovCircle.Thickness = 2
FovCircle.Color = Color3.fromRGB(100, 0, 100) -- Outline color
FovCircle.Filled = false
FovCircle.Transparency = 1 -- Outline color should be fully opaque
FovCircle.Visible = false

-- Function to update FOV outline color
local function UpdateFovColor()
    local colorStr = FovColorPicker.Text
    local r, g, b = colorStr:match("(%d+),(%d+),(%d+)")
    if r and g and b then
        FovCircle.Color = Color3.fromRGB(tonumber(r), tonumber(g), tonumber(b))
    end
end

FovColorPicker.FocusLost:Connect(UpdateFovColor)

-- Function to update FOV size
local function UpdateFovSize()
    local size = tonumber(SizeSlider.Text)
    if size then
        FovCircle.Radius = size
    end
end

SizeSlider.FocusLost:Connect(UpdateFovSize)

-- Toggle FOV visibility
ToggleButton.MouseButton1Click:Connect(function()
    FovCircle.Visible = not FovCircle.Visible
end)

-- Keybind to toggle the GUI
local guiVisible = true
UIS.InputBegan:Connect(function(input)
    if input.KeyCode == Enum.KeyCode.K then
        guiVisible = not guiVisible
        Frame.Visible = guiVisible
    end
end)

-- Update the position of the FOV circle to follow the mouse
RunService.RenderStepped:Connect(function()
    local mousePos = UIS:GetMouseLocation()
    FovCircle.Position = Vector2.new(mousePos.X, mousePos.Y)
end)
