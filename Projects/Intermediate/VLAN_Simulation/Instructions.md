# VLAN Simulation - Intermediate Network Project

## Objective
The goal of this project is to understand and configure **Virtual Local Area Networks (VLANs)** in a simulated network environment. You will learn to:

- Create multiple VLANs on switches
- Assign ports to specific VLANs
- Test communication between VLANs using routing or trunking
- Capture and analyze network traffic

---

## Prerequisites
Before starting this project, ensure you have:

1. Basic knowledge of networking concepts (IP addressing, subnetting, switches)
2. A network simulation tool such as:
   - Cisco Packet Tracer
   - GNS3
   - VirtualBox + Cisco IOS images
3. Access to a terminal for CLI configuration

---

## Topology Overview

Switch1
+----+----+----+----+
| VLAN10 | VLAN20 | VLAN30 |
+----+----+----+----+

PC1 (VLAN10) ---|
PC2 (VLAN10) ---|
PC3 (VLAN20) ---|
PC4 (VLAN20) ---|
PC5 (VLAN30) ---|
PC6 (VLAN30) ---|



- **VLAN10:** Department A  
- **VLAN20:** Department B  
- **VLAN30:** Department C

---

## Tasks

1. **Create VLANs**
   - Configure VLAN10, VLAN20, and VLAN30 on your switch
   - Assign each VLAN a name (optional)

2. **Assign Ports**
   - Assign switch ports to appropriate VLANs based on connected PCs
   - Verify port VLAN assignment using `show vlan brief`

3. **Configure Inter-VLAN Routing** (Optional)
   - Use a router or Layer 3 switch
   - Configure sub-interfaces for each VLAN
   - Assign IP addresses for routing between VLANs

4. **Testing**
   - Test connectivity using `ping` between PCs in the same VLAN
   - Test connectivity between different VLANs (if routing configured)
   - Capture traffic using Packet Tracer simulation or Wireshark

5. **Documentation**
   - Take screenshots of:
     - VLAN configuration
     - Port assignments
     - Test results
   - Save all outputs in `/Results` folder

---

## Expected Outcome

- Each VLAN is isolated from the others unless routing is configured
- PCs within the same VLAN can communicate successfully
- PCs in different VLANs cannot communicate without inter-VLAN routing
- Documentation with screenshots and logs is complete

---

## Notes & Tips

- Always save the switch configuration with `write memory` or `copy running-config startup-config`
- Use descriptive names for VLANs to avoid confusion
- Keep a backup of configuration files in `/Configurations/Intermediate/`

---

## Deliverables

1. `VLAN_Config.txt` - Switch configuration file  
2. `Packet_Capture.pcap` - Optional, network traffic capture  
3. `Results/` - Screenshots of VLAN setup and test pings  
4. `Instructions.md` - This file with steps followed  

---

**Tags / Hashtags:**  
#NetworkEnterprise #Intermediate #VLAN #NetworkSimulation #PacketTracer #GNS3 #LabProject #NetworkingIndonesia
