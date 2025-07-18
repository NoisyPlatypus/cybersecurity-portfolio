# Red Team DoS Assessment - MediCare Health Services

## Project Overview

**Course**: VU23219 - Manage the security infrastructure for an organisation  
**Assessment**: Part C - Collaborative Red, Blue, and Purple Team Exercise  
**Role**: Red Team Member (Individual Contribution)  
**Scenario**: MediCare Health Services Network Security Assessment  
**Completion Date**: June 2025

## Assessment Scenario

As part of a comprehensive cybersecurity exercise, our team was tasked with protecting MediCare Health Services' network infrastructure through collaborative red, blue, and purple team operations:

### Team Roles and Responsibilities

**Red Team (My Role)**: 
- Simulate realistic cyber threats against healthcare infrastructure
- Identify and exploit vulnerabilities to test security measures  
- Focus on Denial of Service (DoS) attack vectors
- Document attack methodology and effectiveness

**Blue Team**: 
- Respond to and defend against simulated attacks
- Identify and remediate discovered vulnerabilities
- Implement defensive countermeasures

**Purple Team**: 
- Analyse attack and defense strategies
- Facilitate collaboration between red and blue teams
- Develop comprehensive security improvement recommendations

## Technical Environment

### Infrastructure Setup
- **Virtualisation Platform**: VMware for isolated testing environment
- **Target System**: Metasploitable 2 (192.168.50.20) simulating healthcare infrastructure
- **Attack Platform**: Kali Linux (192.168.50.10)
- **Network Segment**: 192.168.50.0/24 controlled lab environment

### Healthcare Context Simulation
The exercise specifically targeted healthcare services to understand the critical nature of:
- Patient portal systems and electronic health records
- Online appointment scheduling and telehealth services
- Critical healthcare operational systems
- Regulatory compliance requirements (Privacy Act 1988, My Health Records Act 2012)

## Red Team Assessment Methodology

### Phase 1: Reconnaissance and Target Analysis
- **Network Discovery**: Comprehensive mapping of target infrastructure
- **Service Enumeration**: Identification of running services and potential attack vectors
- **Vulnerability Research**: Analysis of discovered services for known weaknesses

### Phase 2: Attack Planning and Preparation
- **Baseline Testing**: Establishing normal system behaviour for impact measurement
- **Attack Vector Selection**: Focus on HTTP service DoS vulnerability
- **Monitoring Setup**: Real-time attack impact assessment capabilities

### Phase 3: DoS Attack Execution
- **Attack Type**: SYN flood targeting HTTP service (Port 80)
- **Tool Used**: hping3 with randomized source IP addresses
- **Attack Duration**: Controlled 20-second attack window
- **Target**: `hping3 -S -p 80 --flood --rand-source 192.168.50.20`

### Phase 4: Impact Assessment and Documentation
- **Real-time Monitoring**: Multi-terminal observation of service degradation
- **Recovery Analysis**: Assessment of system resilience and recovery capabilities
- **Business Impact Evaluation**: Healthcare-specific consequence analysis

## Critical Findings

### Attack Effectiveness
- **Attack Duration**: 20 seconds controlled execution
- **Impact Duration**: 30+ minutes complete service unavailability
- **Impact Amplification Ratio**: 90:1 (minimal effort, maximum disruption)
- **Recovery Mechanism**: Manual intervention required - no automatic recovery

### Healthcare-Specific Impact Analysis
- **Patient Safety Risks**: Critical test results inaccessible during emergencies
- **Operational Disruption**: Electronic medical records unreachable
- **Compliance Violations**: Potential breaches of healthcare privacy regulations
- **Financial Impact**: Revenue loss, regulatory fines, recovery costs

### Secondary Vulnerabilities Discovered
- **FTP Backdoor**: vsftpd 2.3.4 with CVE-2011-2523 enabling remote code execution
- **Direct System Access**: Bindshell service providing root-level access
- **Outdated Services**: Multiple services with known vulnerabilities

## Skills Demonstrated

### Red Team Operations
- **Attack Simulation**: Realistic threat actor behavior modeling
- **Vulnerability Exploitation**: Practical application of attack methodologies
- **Impact Assessment**: Comprehensive analysis of attack effectiveness
- **Healthcare Context Understanding**: Industry-specific risk evaluation

### Technical Competencies
- **Network Security Testing**: DoS attack execution and measurement
- **Security Tool Proficiency**: Expert use of penetration testing tools
- **System Monitoring**: Real-time attack impact observation
- **Vulnerability Research**: CVE analysis and exploitation techniques

### Professional Security Practices
- **Controlled Testing**: Ethical hacking within defined parameters
- **Risk Communication**: Translation of technical findings to business impact
- **Collaborative Security**: Effective red team operations and documentation
- **Regulatory Awareness**: Understanding of healthcare compliance requirements

## Business Impact Assessment

### Immediate Consequences
- **Service Availability**: Complete HTTP service failure lasting 30+ minutes
- **Patient Care Impact**: Inability to access critical health information
- **Operational Costs**: Manual processes, staff overtime, system recovery
- **Regulatory Risk**: Potential violations of healthcare information access requirements

### Strategic Recommendations
- **Immediate Actions**: Critical vulnerability patching within 24-48 hours
- **Short-term Improvements**: DoS protection and monitoring implementation
- **Long-term Strategy**: Comprehensive security program and resilience planning

## Collaborative Learning Outcomes

### Red Team Expertise
- **Offensive Security**: Practical attack execution and methodology
- **Healthcare Security**: Understanding of industry-specific threats and regulations
- **Impact Analysis**: Comprehensive assessment of attack consequences
- **Professional Documentation**: Industry-standard security reporting

### Cross-Team Collaboration
- **Communication**: Effective coordination with blue and purple teams
- **Knowledge Sharing**: Contributing to comprehensive security assessment
- **Strategic Thinking**: Understanding defensive perspectives and improvements
- **Holistic Security**: Appreciation for complete security lifecycle

## Academic and Professional Context

This collaborative exercise represents advanced cybersecurity education combining:
- **Practical Skills**: Hands-on attack execution and analysis
- **Industry Relevance**: Healthcare sector security challenges
- **Team Collaboration**: Real-world security team dynamics
- **Professional Standards**: Industry-standard documentation and methodology

The assessment successfully demonstrated the critical importance of proactive security testing and the devastating potential of simple attacks against inadequately protected healthcare infrastructure.

---

*This red team assessment was completed as part of advanced cybersecurity coursework at Holmesglen Institute, demonstrating practical offensive security capabilities in a healthcare context while maintaining ethical standards and collaborative professionalism.*